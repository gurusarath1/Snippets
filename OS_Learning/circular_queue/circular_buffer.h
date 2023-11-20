
typedef struct {
       int value;
} q_element;

#define BUF_ARRAY_SIZE (11)
#define BUF_SIZE (BUF_ARRAY_SIZE - 1)

typedef struct {

        int in;
        int out;

        q_element circular_buffer[BUF_SIZE];

} shared_mem_circular_buffer;

#define CIRCULAR_BUF_NAME "smem_c_buf"


