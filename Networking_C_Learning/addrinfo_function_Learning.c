#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define SERVER_PORT 5432
#define MAX_PENDING 5
#define MAX_LINE 256


int main()
{

int status;
struct addrinfo hints;
struct addrinfo *servinfo;
struct addrinfo *p;
struct addrinfo *temp;
struct sockaddr_in *sin ;
char ipstr[INET_ADDRSTRLEN];

//sin = (*sockaddr_in) (servinfo->ai_addr);


memset(&hints, 0, sizeof(hints));
hints.ai_family = AF_UNSPEC;     // don't care IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM; // TCP stream sockets
hints.ai_flags = AI_PASSIVE;     // fill in my IP for me


	if ((status = getaddrinfo("www.google.com", "8080", &hints, &servinfo)) > 0)
	{
		fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
		return 1;
	}

	p = servinfo;

	while (p != NULL)
	{
        char *ipver;
        void *addr;

		printf("%d\n", p->ai_flags);
        printf("%d\n", p->ai_family);
        printf("%d\n", p->ai_socktype);
        printf("%d\n", p->ai_protocol);
        printf("%d\n", p->ai_addrlen);

       if (p->ai_family == AF_INET)
       { // IPv4
            struct sockaddr_in *ipv4 = (struct sockaddr_in *)p->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        }
        else { // IPv6
            struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)p->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }

        // convert the IP to a string and print it:
        inet_ntop(p->ai_family, addr, ipstr, sizeof ipstr);
        printf("  %s: %s\n", ipver, ipstr);

        p = p->ai_next;

	}




	return 0;
}
