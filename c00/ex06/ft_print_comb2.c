#include <unistd.h>

void ft_putchar(char c) {
	write(STDOUT_FILENO, &c, 1);
}

void ft_put2digits(int n) {
	ft_putchar('0' + n/10);
	ft_putchar('0' + n%10);
}

void ft_print_comb2() {
	for (int i = 0; i < 100; i++) {
		for (int j = i+1; j < 100; j++) {
			ft_put2digits(i);
			ft_putchar(' ');
			ft_put2digits(j);
			ft_putchar(',');
			ft_putchar(' ');
		}
	}
}

int main(void) {
	ft_print_comb2();
}
