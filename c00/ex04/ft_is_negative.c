#include <unistd.h>

void ft_is_negative(int n) {
  char buf[1];
  if (n < 0) {
    buf[0] = 'N';
  } else {
    buf[0] = 'P';
  }
  write(STDOUT_FILENO, &buf, 1);
}

int main(void) {
  ft_is_negative(-11);
  ft_is_negative(0);
  ft_is_negative(1);
  return 0;
}
