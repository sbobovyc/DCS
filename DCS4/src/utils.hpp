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

#ifndef UTILS_HPP_
#define UTILS_HPP_

extern "C" void draw_blobs(const int canvas_width, const int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, int ** mask);
extern "C" int test(void);
#endif /* UTILS_HPP_ */
