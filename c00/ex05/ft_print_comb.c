#include <unistd.h>

void ft_putchar(char c) {
  write(STDOUT_FILENO, &c, 1);
}

void ft_print_comb() {
  int i, j, k;
  for (i = 0; i < 10; i++) {
    for (j = i+1; j < 10; j++) {
      for (k = j+1; k < 10; k++) {
	ft_putchar('0'+i);
	ft_putchar('0'+j);
	ft_putchar('0'+k);
	if (!(i==7 && j==8 && k==9)) {
	  ft_putchar(',');
	  ft_putchar(' ');
	}
      }
    }
  }
}

int main(void) {
  ft_print_comb();
}

