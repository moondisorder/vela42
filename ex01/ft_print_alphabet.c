#include <stdio.h>

void ft_print_alphabet(void) {
  for (int i=0; i<26; i++) {
    printf("%c", 'a'+i);
  }
}

int main(void) {
  ft_print_alphabet();
  return 0;
}
