#include <unistd.h>

void ft_print_alphabet(void) {
  for (int i=0; i<26; i++) {
    char c = 'a'+i;
    write(STDOUT_FILENO, &c, 1);
  }
}

int main(void) {
  ft_print_alphabet();
  return 0;
}
