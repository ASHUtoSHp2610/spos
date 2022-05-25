//example2.c
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
void main()
{
	int c,pid,pid1, id, status;
	char *argv[3];
	printf("1.ps\n2.fork\n3.wait\n4.execv\n5.join\n");
	scanf("%dEnter your choice: ",&c);

	switch(c)
	{
		case 1:
			printf("\n#ps#\n");
			system("ps");
			break;
		case 2:
			printf("\n**********fork**********\n");
			pid=fork();
			printf("Hii\n");
			if(pid>0)
			{
				printf("Parent id = %d Child id=%d\n",getpid(),pid);
			}
			else if(pid==0)
			{
				printf("Parent = %d Child = %d\n",getppid(),getpid());
			}
			break;
	   case 3:
	
			//wait
			printf("\n**********fork**********\n");
			pid=fork();
			printf("Hii\n");
			if(pid>0)
			{
				printf("Parent id = %d Child id=%d\n",getpid(),pid);
				id = wait(&status);
				printf("waiting process terminated%d",id);
			}
			else if(pid==0)
			{
				printf("Parent = %d Child = %d\n",getppid(),getpid());
				
			}
			break;
	case 4:		
		printf("\n**********fork**********\n");
			pid=fork();
			printf("Hii\n");
			if(pid>0)
			{
				printf("In Parent process");
			        execv("/usr/bin/firefox",argv);
			}
			else if(pid==0)
			{
				printf("in child process");
				
			}
			break;	
	}
}
