#include <unistd.h>

void newLine(){
	char c = '\n';
	write(STDOUT_FILENO,&c,1);
}

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

void printInt(int n){
	char buf[4];
	buf[0]='0'+n;
	write(STDOUT_FILENO,buf,1);
}

int main(void){
	hello();
	newLine();
	printInt(0);
	newLine();
}
