#define HALIDE_USE_GPU
#include "caffe_input_transformer_base.h"
HALIDE_REGISTER_GENERATOR(CaffeInputTransformer, caffe_input_transformer_gpu);
