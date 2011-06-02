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

namespace DCS {
std::map<Magick::Color, unsigned long> create_histogram(const std::string &image_path);
std::vector<Magick::Color> calculate_colors(std::map<Magick::Color, unsigned long> color_histogram, int number_of_colors);
Magick::Color calculate_base_color(std::vector<Magick::Color> colors);
void draw_blobs(int count, std::vector<int> color, int width, int height, int canvas_width, int canvas_height, int max_level, int distribution[8], Magick::Image * image);
}

#endif /* UTILS_HPP_ */
