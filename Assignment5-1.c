#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int number, space, space2, line,x, number2;
    char special_ch, special_ch2;
    space2 = 0;
    number = atoi(argv[1]);
    number2 = number;
    special_ch = '/';
    special_ch2 = '\\';

    for (line = 0; line < number2; line++){
        for (space = 0; space < number - 1; space++){
            printf(" ");
        }
        printf("%c", special_ch);
        for (x = 0; x < space2; x++){
            printf(" ");
        }
        printf("%c", special_ch2);
        printf("\n");
        number = number - 1;
        space2 = space2 + 2;
    }
    number = 1;
    space2 = (2 * number2) - 2;
    for (line = 0; line < number2; line++){
        for (space = 0; space < number - 1; space++){
            printf(" ");
        }
        printf("%c", special_ch2);
        for (x = 0; x < space2; x++){
            printf(" ");
        }
        printf("%c", special_ch);
        printf("\n");
        number = number + 1;
        space2 = space2 - 2;
    }
    return 0;
}
