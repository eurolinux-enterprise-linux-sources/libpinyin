#include "timer.h"
#include <string.h>
#include "pinyin_internal.h"
#include "tests_helper.h"

size_t bench_times = 1000;

int main(int argc, char * argv[]){
    SystemTableInfo system_table_info;

    bool retval = system_table_info.load("../../data/table.conf");
    if (!retval) {
        fprintf(stderr, "load table.conf failed.\n");
        exit(ENOENT);
    }

    PhraseLargeTable2 largetable;
    FacadePhraseIndex phrase_index;

    const pinyin_table_info_t * phrase_files =
        system_table_info.get_table_info();

    if (!load_phrase_table(phrase_files, NULL, &largetable, &phrase_index))
        exit(ENOENT);

    MemoryChunk * chunk = new MemoryChunk;
    largetable.store(chunk);
    largetable.load(chunk);

    char* linebuf = NULL; size_t size = 0; ssize_t read;
    while ((read = getline(&linebuf, &size, stdin)) != -1) {
        if ( '\n' == linebuf[strlen(linebuf) - 1] ) {
            linebuf[strlen(linebuf) - 1] = '\0';
        }

        if ( strcmp ( linebuf, "quit" ) == 0)
            break;

        glong phrase_len = g_utf8_strlen(linebuf, -1);
        ucs4_t * new_phrase = g_utf8_to_ucs4(linebuf, -1, NULL, NULL, NULL);

        if (0 == phrase_len)
            continue;

        PhraseTokens tokens;
        memset(tokens, 0, sizeof(PhraseTokens));
        phrase_index.prepare_tokens(tokens);

        guint32 start = record_time();
        for (size_t i = 0; i < bench_times; ++i){
            phrase_index.clear_tokens(tokens);
            largetable.search(phrase_len, new_phrase, tokens);
        }
        print_time(start, bench_times);

        phrase_index.clear_tokens(tokens);
        int retval = largetable.search(phrase_len, new_phrase, tokens);

        if (retval & SEARCH_OK) {
            for (size_t i = 0; i < PHRASE_INDEX_LIBRARY_COUNT; ++i) {
                GArray * array = tokens[i];
                if (NULL == array)
                    continue;

                for (size_t k = 0; k < array->len; ++k) {
                    phrase_token_t token = g_array_index
                        (array, phrase_token_t, k);

                    printf("token:%d\t", token);
                }
            }
            printf("\n");
        }

        phrase_index.destroy_tokens(tokens);
        g_free(new_phrase);
    }

    if ( linebuf )
        free(linebuf);

    /* mask out all index items. */
    largetable.mask_out(0x0, 0x0);

    return 0;
}
