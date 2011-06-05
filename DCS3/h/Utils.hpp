/*
 * Utils.hpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#ifndef UTILS_HPP_
#define UTILS_HPP_

#include <vector>
#include <Magick++.h>
#include "DCS_types.hpp"

namespace DCS {
std::map<Magick::Color, unsigned long> create_histogram(const std::string &image_path);
void print_histogram(const DCS_histogram &histogram);
void print_color_vector(const DCS_color_vector &color_vector);
void sort_color_vector(DCS_color_vector &color_vector);
DCS::DCS_color_vector calculate_colors(std::map<Magick::Color, unsigned long> color_histogram, int number_of_colors);
Magick::Color calculate_base_color(DCS::DCS_color_vector);
void draw_blobs(Magick::Color color, int canvas_width, int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, Magick::Image * image);
}

#endif /* UTILS_HPP_ */
