/*
 * DCS_types.hpp
 *
 *  Created on: Jun 2, 2011
 *      Author: sbobovyc
 */

#ifndef DCS_TYPES_HPP_
#define DCS_TYPES_HPP_

namespace DCS{

typedef std::map<Magick::Color, unsigned long> DCS_histogram;
typedef std::vector< std::pair<Magick::Color, unsigned long> > DCS_color_vector;

typedef struct {
	int red;
	int green;
	int blue;
} DCS_universal_color;

inline DCS_universal_color MagickColor_to_DCS_Color(Magick::Color mcolor)
{
	DCS_universal_color dcolor;
	dcolor.red = (double(mcolor.redQuantum()) / 65536.0) * 255.0;
	dcolor.green = (double(mcolor.greenQuantum()) / 65536.0) * 255.0;
	dcolor.blue = (double(mcolor.blueQuantum()) / 65536.0) * 255.0;
	return dcolor;
}

}
#endif /* DCS_TYPES_HPP_ */
