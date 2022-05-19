#include <unistd.h>

void ft_putnbr(int n) {
  // Handle negative numbers.
  if (n < 0) {
    char c = '-';
    write(STDOUT_FILENO, &c, 1);
    ft_putnbr(-n);
    return;
  }
  
  char buf[10]; // Maximum number of digits for 32-bit integer.
  int digits = 0;

  do {
    digits++;
    int d = n % 10; // Get the last digit.
    buf[10-digits] = '0'+d;
    n /= 10;
  } while (n != 0);

  write(STDOUT_FILENO, buf+10-digits, digits);
}

int main(void) {
  char nl = '\n';
  ft_putnbr(0);
  write(STDOUT_FILENO, &nl, 1);
  ft_putnbr(42);
  write(STDOUT_FILENO, &nl, 1);
  ft_putnbr(2147483647);
  write(STDOUT_FILENO, &nl, 1);
  ft_putnbr(-1);
  write(STDOUT_FILENO, &nl, 1);
  ft_putnbr(-2147483647);
  write(STDOUT_FILENO, &nl, 1);
}

