#include <iostream>
#include <iomanip>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>

#include <Magick++.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

using namespace std;
using namespace Magick;

static ColorRGB bg_color = ColorRGB(0.26, 0.35, 0.26);
static ColorRGB color1 = ColorRGB(0.3, 0.3, 0.18);
static ColorRGB color2 = ColorRGB(0.3, 0.4, 0.18);
static int COLOR2_PROB = 20;

int IMG_SIZE = 400;
int HALF_BLOCK_SIZE = 5;
int BLOCK_DENSITY = 300; //the higher, the fewer blocks will be drawn

//recursive drawing parameters
int THRESH = 90;
int DELTA = 5;
int distribution[8]; //inner characteristics
int distribution2[8] = { 5, 5, 5, 5, 5, 5, 5, 5 }; //edge characteristics

bool debug = false;

//http://www.imagemagick.org/Magick++/STL.html

void calc_histogram(char * filename) {

		Image image(filename);
		map<Color, unsigned long> histogram;
		colorHistogram(&histogram, image);
		std::map<Color, unsigned long>::const_iterator p = histogram.begin();

		int bin_size = int(histogram.size()) / 3;
		int low[4] = { 0, 0, 0, 0 };
		int mid[4] = { 0, 0, 0, 0 };
		int high[4] = { 0, 0, 0, 0 };
		p = histogram.begin();

		if(debug)
			cout << "Bin size " << bin_size << endl;

		for (unsigned int i = 0; i < histogram.size(); i++) {
			/*
			 cout << setw(10) << (int)p->second << ": ("
			 << setw(quantum_width) << (int)p->first.redQuantum() << ","
			 << setw(quantum_width) << (int)p->first.greenQuantum() << ","
			 << setw(quantum_width) << (int)p->first.blueQuantum() << ")"
			 << endl;
			 */
			if ((int) i < bin_size) {
				low[0] += (int) p->first.redQuantum() * (int) p->second;
				low[1] += (int) p->first.greenQuantum() * (int) p->second;
				low[2] += (int) p->first.blueQuantum() * (int) p->second;
				low[3] += (int) p->second;
				//cout << p->second << endl;
			} else if ((int) i > bin_size && (int) i < 2 * bin_size) {
				mid[0] += (int) p->first.redQuantum() * (int) p->second;
				mid[1] += (int) p->first.greenQuantum() * (int) p->second;
				mid[2] += (int) p->first.blueQuantum() * (int) p->second;
				mid[3] += (int) p->second;
			} else {
				high[0] += (int) p->first.redQuantum() * (int) p->second;
				high[1] += (int) p->first.greenQuantum() * (int) p->second;
				high[2] += (int) p->first.blueQuantum() * (int) p->second;
				high[3] += (int) p->second;
			}
			p++;
		}

		low[0] /= low[3];
		low[1] /= low[3];
		low[2] /= low[3];
		mid[0] /= mid[3];
		mid[1] /= mid[3];
		mid[2] /= mid[3];
		high[0] /= high[3];
		high[1] /= high[3];
		high[2] /= high[3];

		if (debug) {
			cout << low[0] << " " << low[1] << " " << low[2] << " " << low[3]
					<< endl;
			cout << mid[0] << " " << mid[1] << " " << mid[2] << " " << mid[3]
					<< endl;
			cout << high[0] << " " << high[1] << " " << high[2] << " "
					<< high[3] << endl;
		}

		//sort the colors by order of frequency
		int color[3][4];
		if (mid[3] < low[3] && mid[3] < high[3]) {
			color[2][0] = mid[0];
			color[2][1] = mid[1];
			color[2][2] = mid[2];
			color[2][3] = mid[3];
			if (low[3] < high[3]) {
				color[0][0] = high[0];
				color[0][1] = high[1];
				color[0][2] = high[2];
				color[0][3] = high[3];
				color[1][0] = low[0];
				color[1][1] = low[1];
				color[1][2] = low[2];
				color[1][3] = low[3];
			} else {
				color[0][0] = low[0];
				color[0][1] = low[1];
				color[0][2] = low[2];
				color[0][3] = low[3];
				color[1][0] = high[0];
				color[1][1] = high[1];
				color[1][2] = high[2];
				color[1][3] = high[3];
			}
		} else if (low[3] < high[3]) {
			color[2][0] = low[0];
			color[2][1] = low[1];
			color[2][2] = low[2];
			color[2][3] = low[3];
			if (mid[3] < high[3]) {
				color[0][0] = high[0];
				color[0][1] = high[1];
				color[0][2] = high[2];
				color[0][3] = high[3];
				color[1][0] = mid[0];
				color[1][1] = mid[1];
				color[1][2] = mid[2];
				color[1][3] = mid[3];
			} else {
				color[0][0] = mid[0];
				color[0][1] = mid[1];
				color[0][2] = mid[2];
				color[0][3] = mid[3];
				color[1][0] = high[0];
				color[1][1] = high[1];
				color[1][2] = high[2];
				color[1][3] = high[3];
			}
		} else {
			color[2][0] = high[0];
			color[2][1] = high[1];
			color[2][2] = high[2];
			color[2][3] = high[3];
			if (mid[3] < low[3]) {
				color[0][0] = low[0];
				color[0][1] = low[1];
				color[0][2] = low[2];
				color[0][3] = low[3];
				color[1][0] = mid[0];
				color[1][1] = mid[1];
				color[1][2] = mid[2];
				color[1][3] = mid[3];
			} else {
				color[0][0] = mid[0];
				color[0][1] = mid[1];
				color[0][2] = mid[2];
				color[0][3] = mid[3];
				color[1][0] = low[0];
				color[1][1] = low[1];
				color[1][2] = low[2];
				color[1][3] = low[3];
			}
		}

		if (debug) {
			cout << "Sorted colors: " << endl;
			for (int i = 0; i < 3; i++)
				cout << color[i][0] << " " << color[i][1] << " " << color[i][2]
						<< endl;
		}

		bg_color = ColorRGB(float(color[0][0]) / 255.0f, float(color[0][1])
				/ 255.0f, float(color[0][2]) / 255.0f);
		color1 = ColorRGB(float(color[1][0]) / 255.0f, float(color[1][1])
				/ 255.0f, float(color[1][2]) / 255.0f);
		color2 = ColorRGB(float(color[2][0]) / 255.0f, float(color[2][1])
				/ 255.0f, float(color[2][2]) / 255.0f);

		COLOR2_PROB = 100 * color[2][3] / ( color[2][3] + color[1][3] + color[0][3]);

		if(debug){
			cout << "Second color probability: " << COLOR2_PROB << endl;
		}


}

int calc_blocks(int width, int height, int block_size) {
	return (width * height) / (block_size * BLOCK_DENSITY);
}

void set_distribution(int select) {
	switch (select) {
	case 0: //blotch
		distribution[0] = 30;
		distribution[1] = 30;
		distribution[2] = 30;
		distribution[3] = 30;
		distribution[4] = 30;
		distribution[5] = 30;
		distribution[6] = 30;
		distribution[7] = 30;
		for (int i = 0; i < 8; i++)
			distribution2[i] = 20;

		break;
	case 1: //rain drop
		distribution[0] = 15;
		distribution[1] = 70;
		distribution[2] = 15;
		distribution[3] = 5;
		distribution[4] = 5;
		distribution[5] = 15;
		distribution[6] = 70;
		distribution[7] = 15;
		distribution2[1] = 30;
		distribution2[6] = 30;
		break;
	case 2: //tiger stripe
		distribution[0] = 10;
		distribution[1] = 5;
		distribution[2] = 10;
		distribution[3] = 90;
		distribution[4] = 90;
		distribution[5] = 10;
		distribution[6] = 5;
		distribution[7] = 10;
		distribution2[3] = 90;
		distribution2[4] = 90;
		break;
	default:
		break;
	}

}
void draw_patch(int x_coord, int y_coord, int p, int d, Image & image) {

	if (debug) {
		image.strokeColor("red"); // Outline color
		image.strokeWidth(2);
	}
	// Draw a rectangle
	image.draw(DrawableRectangle(x_coord - HALF_BLOCK_SIZE, y_coord
			- HALF_BLOCK_SIZE, x_coord + HALF_BLOCK_SIZE, y_coord
			+ HALF_BLOCK_SIZE));

	if (p >= THRESH) {
		if (rand() % 100 <= distribution[0]) {
			//cout << "0" << endl;
			draw_patch(x_coord - 2 * HALF_BLOCK_SIZE, y_coord + 2
					* HALF_BLOCK_SIZE, p - d, d, image);
		}
		if (rand() % 100 <= distribution[1]) {
			//cout << "1" << endl;
			draw_patch(x_coord, y_coord + 2 * HALF_BLOCK_SIZE, p - d, d, image);
		}
		if (rand() % 100 <= distribution[2]) {
			//cout << "2" << endl;
			draw_patch(x_coord + 2 * HALF_BLOCK_SIZE, y_coord + 2
					* HALF_BLOCK_SIZE, p - d, d, image);
		}
		if (rand() % 100 <= distribution[3]) {
			//cout << "3" << endl;
			draw_patch(x_coord - 2 * HALF_BLOCK_SIZE, y_coord, p - d, d, image);
		}
		if (rand() % 100 <= distribution[4]) {
			//cout << "4" << endl;
			draw_patch(x_coord + 2 * HALF_BLOCK_SIZE, y_coord, p - d, d, image);
		}
		if (rand() % 100 <= distribution[5]) {
			//cout << "5" << endl;
			draw_patch(x_coord - 2 * HALF_BLOCK_SIZE, y_coord - 2
					* HALF_BLOCK_SIZE, p - d, d, image);
		}
		if (rand() % 100 <= distribution[6]) {
			//cout << "6" << endl;
			draw_patch(x_coord, y_coord - 2 * HALF_BLOCK_SIZE, p - d, d, image);
		}
		if (rand() % 100 <= distribution[7]) {
			//cout << "7" << endl;
			draw_patch(x_coord + 2 * HALF_BLOCK_SIZE, y_coord - 2
					* HALF_BLOCK_SIZE, p - d, d, image);
		}

	} else {
		if (rand() % 100 <= distribution2[0]) {
			image.draw(DrawableRectangle(x_coord - 3 * HALF_BLOCK_SIZE, y_coord
					+ HALF_BLOCK_SIZE, x_coord - HALF_BLOCK_SIZE, y_coord + 3
					* HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[1]) {
			image.draw(DrawableRectangle(x_coord - HALF_BLOCK_SIZE, y_coord
					+ HALF_BLOCK_SIZE, x_coord + HALF_BLOCK_SIZE, y_coord + 3
					* HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[2]) {
			image.draw(DrawableRectangle(x_coord + HALF_BLOCK_SIZE, y_coord
					+ HALF_BLOCK_SIZE, x_coord + 3 * HALF_BLOCK_SIZE, y_coord
					+ 3 * HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[3]) {
			image.draw(DrawableRectangle(x_coord - 3 * HALF_BLOCK_SIZE, y_coord
					- HALF_BLOCK_SIZE, x_coord - HALF_BLOCK_SIZE, y_coord
					+ HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[4]) {
			image.draw(DrawableRectangle(x_coord + HALF_BLOCK_SIZE, y_coord
					- HALF_BLOCK_SIZE, x_coord + 3 * HALF_BLOCK_SIZE, y_coord
					+ HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[5]) {
			image.draw(DrawableRectangle(x_coord - 3 * HALF_BLOCK_SIZE, y_coord
					- HALF_BLOCK_SIZE, x_coord - HALF_BLOCK_SIZE, y_coord - 3
					* HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[6]) {
			image.draw(DrawableRectangle(x_coord - HALF_BLOCK_SIZE, y_coord
					- HALF_BLOCK_SIZE, x_coord + HALF_BLOCK_SIZE, y_coord - 3
					* HALF_BLOCK_SIZE));
		}
		if (rand() % 100 <= distribution2[7]) {
			image.draw(DrawableRectangle(x_coord + HALF_BLOCK_SIZE, y_coord
					- HALF_BLOCK_SIZE, x_coord + 3 * HALF_BLOCK_SIZE, y_coord
					- 3 * HALF_BLOCK_SIZE));
		}
	}
}

void web_driver(char & filename, char & outfile, int distribution) {
	CvCapture *capture = NULL;
	IplImage *frame = NULL;

	/* initialize camera */

	capture = cvCaptureFromCAM(0);
	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 640);
	cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 480);

	/* always check */

	if (!capture) {

		fprintf(stderr, "Cannot open initialize webcam!\n");

		exit(1);

	}

	/* create a window for the video */

	cvNamedWindow("Webcam", CV_WINDOW_AUTOSIZE);

	while (cvWaitKey(10) != 'q') {

		/* get a frame */

		frame = cvQueryFrame(capture);

		/* always check */

		if (!frame) {
			exit(1);
			//break;
		}

		/* display current frame */
		cvSmooth(frame, frame, CV_BLUR, 10, 3);
		// CV_BLUR_NO_SCALE, CV_BLUR, CV_GAUSSIAN, CV_MEDIAN, CV_BILATERAL
		cvShowImage("Webcam", frame);

		cvSaveImage(&filename, frame);

		set_distribution(distribution);
		int num_blocks = calc_blocks(IMG_SIZE, IMG_SIZE, 2 * HALF_BLOCK_SIZE);
		calc_histogram(&filename);
		// Create base image
		Image image(Geometry(IMG_SIZE, IMG_SIZE), Color(bg_color));

		srand( time(NULL));
		for (int i = 0; i <= num_blocks; i++) {
			//cout << "Drawing block number: " << i << endl;
			int x_coord = rand() % IMG_SIZE; // x center
			int y_coord = rand() % IMG_SIZE; // y center
			// Set draw options
			if (rand() % 100 > COLOR2_PROB) {
				image.fillColor(color1); // Fill color
			} else {
				image.fillColor(color2); // Fill color
			}
			draw_patch(x_coord, y_coord, 100, DELTA, image);
		}

		//image.gaussianBlur(10.0, 3.0);
		// Display the result

		image.write(&outfile);

		cvShowImage("Camo", cvLoadImage(&outfile));

	}

	/* free memory */

	cvDestroyWindow("Webcam");
	cvDestroyWindow("Camo");
	cvReleaseCapture(&capture);
}

// this driver is obsolete
void driver(char & filename, char & outfile, int distribution) {
	try {

		set_distribution(distribution);
		int num_blocks = calc_blocks(IMG_SIZE, IMG_SIZE, 2 * HALF_BLOCK_SIZE);
		if(&filename != NULL)
			calc_histogram(&filename);
		// Create base image
		Image image(Geometry(IMG_SIZE, IMG_SIZE), Color(bg_color));

		srand( time(NULL));
		for (int i = 0; i <= num_blocks; i++) {
			//cout << "Drawing block number: " << i << endl;
			int x_coord = rand() % IMG_SIZE; // x center
			int y_coord = rand() % IMG_SIZE; // y center
			// Set draw options
			if (rand() % 100 > COLOR2_PROB) {
				image.fillColor(color1); // Fill color
			} else {
				image.fillColor(color2); // Fill color
			}
			draw_patch(x_coord, y_coord, 100, DELTA, image);
		}

		//image.gaussianBlur(10.0, 3.0);
		// Display the result
		image.display();
		if(&outfile == NULL) {
			image.write("out.jpg");
		} else {
			image.write(&outfile);
		}
	} catch (exception &error_) {
		cout << "Caught exception: " << error_.what() << endl;
	}
}

int main(int argc, char **argv) {
	char * filename = NULL;
	char * outfile = NULL;
	int distribution = 0;
	int using_webcam = 0;

	int c;
	bool loop = true;

	while (loop) {
		static struct option long_options[] = {

		/* These options don't set a flag.
		 We distinguish them by their indices. */
		{ "help", no_argument, NULL, 'h' },
		{ "block-geometry", required_argument, 0, 'b' },
		{ "density", required_argument, 0, 'd' },
		{ "style", required_argument, 0, 's' },
		{ "second-color", required_argument, 0, 'c' },
		{ "file", required_argument, 0,'f' },
		{ "out-geometry", required_argument, 0,'o' },
		{ "threshold", required_argument, 0,'t' },
		{ "delta", required_argument, 0,'e' },
		{ "outfile", required_argument, 0,'F' },
		{ "webcam", no_argument, &using_webcam, 1},

		{ 0, 0, 0, 0 }
		};
		/* getopt_long stores the option index here. */
		int option_index = 0;

		c = getopt_long(argc, argv, "hb:d:s:c:f:o:t:e:F:", long_options,
				&option_index);
		switch (c) {
		case 0:
			/* If this option set a flag, do nothing else now. */
			if (long_options[option_index].flag != 0)
				break;
			printf("option %s", long_options[option_index].name);
			if (optarg)
				printf(" with arg %s", optarg);
			printf("\n");
			break;

		case 'h' :
		        std::cout
		          << "Dynamic Camouflage System (Alpha)"
		          << argv[0] << " [--help|-h]" << endl
		          << "     [--block-geometry|-b BLOCK_SIZE] [--density|-d BLOCK_DENSITY " << endl
		          << "     [--style|-s STYLE] [--second-color|-c PROBABILITY] " << endl
		          << "     [--out-geometry|-o SIZE] [--file|-f INFILE]  " << endl
		          << "     [--threshold|-t THR] [--delta|-e DEL] " << endl
		          << "     [--webcam [--outfile|-F OUTFILE] " << endl

		          << endl
		          << "* Options *" << endl
		          << " --help			Print this message" << endl
		          << " --block-geometry	Half the length of the side of the pixel box" << endl
		          << " --density		Density of the generated camouflage. Default=300. The higher the number, the less dense the camouflage." << endl
		          << " --style		0=blotch, 1=rain drop, 2=tiger stripe" << endl
		          << " --threshold=THR	Sentinel value for blotch drawing. Default=90." << endl
		          << " --delta=DEL		Change in starting value during iterations of blotch drawing. Default=5." << endl
		          << " --out-geometry=SIZE	Dimensions of output image. Width=SIZE Height=SIZE." << endl
		          << " --file=INFILE		Input image file." << endl
		          << " --outfile=OUTFILE		Output camouflage to image file." << endl

		          << endl
		          << " * Examples *" << endl
		          << argv[0] << " --file input.jpg --outfile out.jpg" << endl
		          << endl;

		case 'b':
			HALF_BLOCK_SIZE = atoi(optarg);
			break;
		case 'd':
			BLOCK_DENSITY = atoi(optarg);
			break;
		case 's':
			distribution = atoi(optarg);
			break;
		case 'c':
			COLOR2_PROB = atoi(optarg);
			break;
		case 'f':
			filename = optarg;
			break;
		case 'o':
			IMG_SIZE = atoi(optarg);
			break;
		case 't':
			THRESH = atoi(optarg);
			break;
		case 'e':
			DELTA = atoi(optarg);
			break;
		case 'F':
			outfile = optarg;
			break;
		case '?':
			/* getopt_long already printed an error message. */
			exit(1);
			break;

		default:
			loop = false;
		}
	}


	//driver(*filename, *outfile, distribution);
	if(using_webcam == 1){
		char filename[] = "/tmp/out.jpg";
		char outfile[] = "/tmp/out2.jpg";
		web_driver(*filename, *outfile, distribution);
	} else {
		driver(*filename, *outfile, distribution);
	}
	return EXIT_SUCCESS;
}
