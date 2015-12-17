#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sstream> // for converting the command line parameter to integer
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <image_transport/camera_publisher.h>
#include <camera_info_manager/camera_info_manager.h>



int main(int argc, char** argv)
{
   // Check if video source has been passed as a parameter
  //if(argv[1] == NULL) return 1;

  ros::init(argc, argv, "image_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("image_rect", 1);
  //image_transport::Publisher pub2 = it.advertise("camera_info", 1);
  ros::Publisher cam = nh.advertise<sensor_msgs::CameraInfo>("camera_info", 1);
  image_transport::CameraPublisher cp;
  //camera_info_manager::CameraInfoManager cim(nh);
  //cim.loadCameraInfo("/dev/video0");
  //sensor_msgs::CameraInfo tp;
  //image_transport::Publisher cam = it.advertise("camera_info",1);

   // Convert the passed as command line parameter index for the video device to an integer
   //std::istringstream video_sourceCmd(argv[1]);
   //int video_source;
   // Check if it is indeed a number
   //if(!(video_sourceCmd >> video_source)) return 1;
   cv::VideoCapture cap(0);
   // Check if video device can be opened with the given index
   if(!cap.isOpened()) return 1;
   cv::Mat frame;
   sensor_msgs::ImagePtr msg;
 
   ros::Rate loop_rate(5);
   while (nh.ok()) {
     cap >> frame;
     // Check if grabbed frame is actually full with some content
     if(!frame.empty()) {
       msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
       //sensor_msgs::CameraInfo tp(cim.getCameraInfo());
       //tp= &ci;
      pub.publish(msg);
      //cam.publish(tp);
    cv::waitKey(1);
  }
  ros::spinOnce();
  loop_rate.sleep();
}
 }