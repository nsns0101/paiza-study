// 2016년 a월 b일은 무슨요일인지 찾기.
// a, b는 입력받기
// 일요일 ~ 토요일 순서로 SUN, MON, TUE, WED, THU, FRI, SAT


import java.util.*;
public class day{

    public static String solution(int a, int b){
        String answer = "";

        int month[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String day[] = { "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};

        int allday = 0;

        for(int i = 0; i < a - 1; i++){
            allday += month[i];
        }

        allday = allday + b;

        answer = day[allday % 7];

        return answer;
    }

    public static void main(String[] args){
        System.out.println(solution(5,24));
    }
}