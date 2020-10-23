import java.util.*;

public class Solution {
    // p = AM, PM 
    // n = 시간초
    public String solution(String p, int n) {
        // 처음엔 AM(PM) 00:00:00형태로
        // 초 후에는 24시간 시계로 00:00:00
        // ex) PM 05:35:27이 입력되면
        
        //AM또는 PM과 공백지우기 
        String word = p.substring(3);
        // 00:00:00형태를 :로 나눠 배열로 만들기
        String[] split_word = word.split(":");

        //초로 변경
        int Hour = Integer.parseInt(split_word[0]) * 3600;
        int Min = Integer.parseInt(split_word[1]) * 60;
        int Sec = Integer.parseInt(split_word[2]);
        
        //전부 더하기
        int time = Hour + Min + Sec;

        //n시간초 후의 결과
        int result = time + n;

        //PM시간이면
        if(p.contains("P")){
            result += 12 * 60 * 60;
        } 
        //24시가 넘으면 0초로 초기화
        if(result >= 24 * 60 * 60){
            result -= 24*60*60;
        } 
        
        //2400초면 0시간 40분
        String str_hour = result / 3600 + "";
        String str_min = (result % 3600) / 60 + "";
        String str_sec = ((result % 3600) % 60) % 60 + "";
        
        if(str_hour.length() <= 1){
            str_hour = "0".concat(str_hour);
        }
        if(str_min.length() <= 1){
            str_min = "0".concat(str_min);
        }
        if(str_sec.length() <= 1){
            str_sec = "0".concat(str_sec);
        }

        String answer = str_hour + ":" + str_min + ":" + str_sec;
        return answer;
    }
}