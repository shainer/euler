#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char *InputFile(FILE *c)
{
	int i = 0;
	char *array = (char *)malloc(1202 * sizeof(char));
	
	for (i=0; i<1201; i++)
		fscanf(c, "%d", &array[i]);
	
	return array;
}

char *Decrypt(int key1, int key2, int key3, char *old)
{
	int keys[3] = {key1, key2, key3};
	int i;
	char *decrypted = (char *)malloc(1202 * sizeof(char));
	int count = 0;
	
	for (i=0; i<1201; i++) {
		decrypted[i] = old[i] ^ keys[i % 3];
		if (!isprint(decrypted[i]))
			return "None";
	}
			
	decrypted[i] = 0;
	return decrypted;
}

int main(int argc, char **argv)
{
	int char1, char2, char3;
	char *s, *input;
	FILE *crypt = fopen("cipher1.txt", "r");
	input = InputFile(crypt);
	
	
	for (char1 = 97; char1 <= 122; char1++) {
		for (char2 = 97; char2 <= 122; char2++) {
			for (char3 = 97; char3 <= 122; char3++) {
				s = Decrypt(char1, char2, char3, input);

				if (s != "None")
					printf("%d %d %d: %s\n", char1, char2, char3, s);
			}
		}
	}
	
	fclose(crypt);
	return 0;
}
