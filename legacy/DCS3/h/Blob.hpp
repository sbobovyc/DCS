/*
 * Blob.h
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#ifndef BLOB_HPP_
#define BLOB_HPP_

#include <vector>
#include <iostream>

namespace DCS {
class DCS_Blob {
	std::vector<int> color;
	int height;
	int width;
	int canvas_width;
	int canvas_height;
	int current_level;
	int max_level;
	std::pair<int,int> seed_coords;
	std::vector< std::pair< std::pair<int,int>, std::pair<int,int> > > rectangle_list;
	int distribution[8];
	int regression[8];
public:
	DCS_Blob(std::vector<int> color, int width, int height, int canvas_width, int canvas_height, int max_level, std::pair<int,int> seed_coords, int distribution[8]);
	void Build(int, std::pair<int,int>);
	int Random();
	std::vector< std::pair< std::pair<int,int>, std::pair<int,int> > > get_rectangle_list();
	virtual ~DCS_Blob();
	friend std::ostream & operator<< (std::ostream & out, DCS_Blob const & blob);
};

std::ostream & operator<< (std::ostream & out, DCS_Blob const & blob);

}

#endif /* BLOB_HPP_ */
