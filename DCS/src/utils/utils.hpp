/*
 * @file utils.hpp
 *
 * @date Jun 22, 2011
 * @author sbobovyc
 * @description
 * @note
 * See the following for explanation of why extern "C" was used:
 * http://www.parashift.com/c++-faq-lite/mixing-c-and-cpp.html
 * http://wolfprojects.altervista.org/articles/dll-in-c-for-python/
 */
/*
    Copyright (C) 2011 Stanislav Bobovych

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#ifndef UTILS_HPP_
#define UTILS_HPP_

extern "C" void draw_blobs(const int canvas_width, const int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, int ** mask);
extern "C" int test(void);
#endif /* UTILS_HPP_ */
