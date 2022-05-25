#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main()
{
	int c,pid,pid1,id,status;
	char *argv[3];
	printf("1 ps\n2 fork\n3 wait\n4 exec\n\n");
	scanf("%d ",&c);

	switch(c)
	{
		case 1:
			printf("\n PS \n");
			system("ps");
			break;
		case 2:
			printf("\nFORK\n");
			pid = fork();
			if(pid>0)
			{
				printf("Parent id = %d Child ID = %d \n",getpid(),pid);

			}
			else if(pid == 0)
			{
				printf("Parent id = %d Child ID = %d \n",getppid(),getpid());
			}
			break;
		case 3:
			printf("\n Wait \n");
			pid = fork();
			if(pid>0)
			{
				printf("Parent id = %d Child ID = %d \n",getpid(),pid);
				id = wait(&status);
				printf("Waiting process terminated %d\n",id );
			}
			else if(pid == 0)
			{
				printf("Parent id = %d Child ID = %d \n",getppid(),getpid());
			}
			break;

		case 4:
			printf("\n EXEC \n");
			pid = fork();

			if(pid>0)
			{
				printf("Parent id = %d Child ID = %d \n",getpid(),pid);
				execv("/usr/bin/firefox",argv);
			}
			else if(pid == 0)
			{
				printf("Parent id = %d Child ID = %d \n",getppid(),getpid());
			}
			break;
	}

}
