#include <stdio.h>

void ft_is_negative(int n) {
  if (n < 0) {
    printf("N");
  } else {
    printf("P");
  }
}

int main(void) {
  ft_is_negative(-11);
  ft_is_negative(0);
  ft_is_negative(1);
  return 0;
}
