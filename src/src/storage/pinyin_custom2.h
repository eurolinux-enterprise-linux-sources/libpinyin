/* 
 *  libpinyin
 *  Library to deal with pinyin.
 *  
 *  Copyright (C) 2011 Peng Wu <alexepico@gmail.com>
 *  
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 * 
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *  GNU General Public License for more details.
 *  
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#ifndef PINYIN_CUSTOM2_H
#define PINYIN_CUSTOM2_H

#include <glib.h>

G_BEGIN_DECLS

/**
 * PinyinTableFlag:
 */
enum PinyinTableFlag{
    IS_CHEWING = 1U << 1,
    IS_PINYIN = 1U << 2,
    PINYIN_INCOMPLETE = 1U << 3,
    CHEWING_INCOMPLETE = 1U << 4,
    USE_TONE = 1U << 5,
    USE_DIVIDED_TABLE = 1U << 6,
    USE_RESPLIT_TABLE = 1U << 7,
    DYNAMIC_ADJUST = 1U << 8
};

/**
 * PinyinAmbiguity2:
 *
 * The enums of pinyin ambiguities.
 *
 */
enum PinyinAmbiguity2{
    PINYIN_AMB_C_CH = 1U << 9,
    PINYIN_AMB_S_SH = 1U << 10,
    PINYIN_AMB_Z_ZH = 1U << 11,
    PINYIN_AMB_F_H = 1U << 12,
    PINYIN_AMB_G_K = 1U << 13,
    PINYIN_AMB_L_N = 1U << 14,
    PINYIN_AMB_L_R = 1U << 15,
    PINYIN_AMB_AN_ANG = 1U << 16,
    PINYIN_AMB_EN_ENG = 1U << 17,
    PINYIN_AMB_IN_ING = 1U << 18,
    PINYIN_AMB_ALL = 0x3FFU << 9
};

/**
 * PinyinCorrection2:
 *
 * The enums of pinyin corrections.
 *
 */

enum PinyinCorrection2{
    PINYIN_CORRECT_GN_NG = 1U << 21,
    PINYIN_CORRECT_MG_NG = 1U << 22,
    PINYIN_CORRECT_IOU_IU = 1U << 23,
    PINYIN_CORRECT_UEI_UI = 1U << 24,
    PINYIN_CORRECT_UEN_UN = 1U << 25,
    PINYIN_CORRECT_UE_VE = 1U << 26,
    PINYIN_CORRECT_V_U = 1U << 27,
    PINYIN_CORRECT_ON_ONG = 1U << 28,
    PINYIN_CORRECT_ALL = 0xFFU << 21
};

/**
 * @brief enums of Double Pinyin Schemes.
 */
enum DoublePinyinScheme
{
    DOUBLE_PINYIN_ZRM        = 1,
    DOUBLE_PINYIN_MS         = 2,
    DOUBLE_PINYIN_ZIGUANG    = 3,
    DOUBLE_PINYIN_ABC        = 4,
    DOUBLE_PINYIN_PYJJ       = 6,
    DOUBLE_PINYIN_XHE        = 7,
    DOUBLE_PINYIN_CUSTOMIZED = 30,        /* for user's keyboard */
    DOUBLE_PINYIN_DEFAULT    = DOUBLE_PINYIN_MS
};

/**
 * @brief enums of Chewing Schemes.
 */
enum ChewingScheme
{
    CHEWING_STANDARD = 1,
    CHEWING_IBM      = 2,
    CHEWING_GINYIEH  = 3,
    CHEWING_ETEN     = 4,
    CHEWING_DEFAULT  = CHEWING_STANDARD
};

G_END_DECLS

#endif
