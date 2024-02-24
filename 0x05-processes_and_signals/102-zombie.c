#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Runs infinitely
 *
 * Return: Nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		/* Parent */
		if (child_pid > 0)
			printf("Zombie process created, PID: %d\n", getpid());
		/* Child */
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
