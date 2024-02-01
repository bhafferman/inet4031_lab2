#include <stdio.h>
              
               int main() {
              
                 int a = 2;
                 int b = 2;
                 int c = a + b;
              
                 printf("C says: Hello, World!\n");
                 printf("%d + %d = %d\n",a,b,c);
                 char* user_array[] = {"User1", "User2", "User2"};
                 
		 for (int i = 0; i < sizeof(user_array) / sizeof(user_array[0]); i++) {
        		printf("%s\n", user_array[i]);
    		} // for
		// printf("\n");
return 0;
}
