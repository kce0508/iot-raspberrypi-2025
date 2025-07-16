#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DB_FILE "userFile.txt"
#define MAX_LEN 64

int id_exists(const char *id)
{
	FILE *fp = fopen(DB_FILE, "r");
	if (!fp) return 0;

	char file_id[MAX_LEN], file_pw[MAX_LEN];
	while (fscanf(fp, "%63s %63s", file_id, file_pw) == 2) {
		if (strcmp(file_id, id) == 0) {
			fclose(fp);
			return 1;
		}
	} 
	fclose(fp);
	return 0;
}

void signup(void) {
	char id[MAX_LEN], pw[MAX_LEN];

	printf("회원가입\n");
	printf("아이디 입력: ");
	scanf("%63s", id);

	if (id_exists(id)) {
		printf("이미 존재하는 아이디입니다.\n");
		return;
	}

	printf("비밀번호 입력: ");
	scanf("%63s", pw);

	FILE *fp = fopen(DB_FILE, "a");
	if (!fp) {
		perror("파일 열기 실패");
		return;
	}

	fprintf(fp, "%s %s\n", id, pw);
	fclose(fp);
	printf("회원가입 완료!\n");
}

void login(void) {
	char id[MAX_LEN], pw[MAX_LEN];
	printf("로그인\n");
	printf("아이디 입력: ");
	scanf("%63s", id);
	printf("비밀번호 입력: ");
	scanf("%63s", pw);

	FILE *fp = fopen(DB_FILE, "r");
	if (!fp) {
		printf("아직 등록된 사용자가 없습니다.\n");
		return;
	}

	char file_id[MAX_LEN], file_pw[MAX_LEN];
	while (fscanf(fp, "%63s %63s", file_id, file_pw) == 2) {
		if (strcmp(file_id, id) == 0 && strcmp(file_pw, pw) == 0) {
			printf("로그인 성공, %s\n", id);
			fclose(fp);
			return; 
		}
	}
	fclose(fp);
	printf("로그인 실패: 아이디 또는 비밀번호가 틀렸습니다.\n");
}

int main(void)
{
	int choice;
	do {
		printf("\n1) 회원가입\n2) 로그인\n0) 종료\n선택: ");
		if(scanf("%d", &choice) != 1) break;
		switch (choice) {
			case 1: signup(); break;
			case 2: login(); break;
			case 0: puts("프로그램 종료"); break;
			default: puts("잘못된 선택");
		}
	} while (choice != 0);
	return 0;
}

