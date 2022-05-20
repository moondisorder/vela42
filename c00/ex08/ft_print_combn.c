#include <unistd.h>

void ft_putchar(char c) {
	write(STDOUT_FILENO, &c, 1);
}

void ft_print_n_digits(int n, int idx[]) {
	for (int d = 0; d < n; d++) {
		ft_putchar('0' + idx[d]);
	}
	ft_putchar(',');
}

void ft_print_combn(int i, int n, int dig[]) {
	int from;
	if (i > 0) {
		from = dig[i-1]+1;
	} else {
		from = 0;
	}
	
	for (dig[i] = from; dig[i] < 10; dig[i]++) {
		 if (i == n-1) {
				ft_print_n_digits(n, dig);
		 } else {
				ft_print_combn(i+1, n, dig);
		 }
	}
}

int main(void) {
	int dig[10];
	for (int n=1; n < 10; n++) {
		ft_putchar('n');
		ft_putchar('=');
		ft_putchar('0'+n);
		ft_putchar(':');
		ft_putchar('\n');
		ft_print_combn(0, n, dig);
		ft_putchar('\n');
	}
}
