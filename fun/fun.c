#include <unistd.h>

void hello(){
	char buf[6];
	buf[0]='h';
	buf[1]='e';
	buf[2]='l';
	buf[3]='l';
	buf[4]='o';
	buf[5]='\n';

	write(STDOUT_FILENO,buf,6);
}

int main(void){
	hello();
}
