// 양 옆의 사람이 여벌 옷을 들고 있는지 확인하는 것이 핵심
// 처음 사람은 왼쪽사람이 없고, 마지막 사람은 오른쪽 사람이 없음
// 맨 왼쪽, 맨 오른쪽 1칸씩 추가해서 하기
// 옷 없는 학생은 - 1, 여벌 옷 있는 학생은 1, 자기 꺼만 있으면 0
// 왼쪽이나 오른쪽에서 1인 사람이 있으면 옷을 빌리고 값 업데이트 하기
import java.util.ArrayList;
import java.util.Collections;

class Solution{
    public int solution(int n, int[] lost, int[] reserve) {
        int[] clothes = new int[n+2];
        int answer = n;
        clothes[0] = -10;
        clothes[n+1] = -10;


        for(int i=0; i<lost.length; i++){
            clothes[lost[i]] -= 1;
        }

        for(int i=0; i<reserve.length; i++){
            clothes[reserve[i]] += 1;
        }

        for(int i=0; i<=n; i++){
            // 체육복이 없다면
            if(clothes[i] == -1){
                // 왼쪽 학생이 여벌 옷이 있다면 빌림
                if(clothes[i-1] == 1){
                    clothes[i-1] -= 1;
                    clothes[i] += 1;
                }
                // 오른쪽 학생이 여별 옷이 있다면 빌림
                else if(clothes[i+1] == 1){
                    clothes[i+1] -= 1;
                    clothes[i] += 1;
                }
                // 빌릴 수 없다면
                else{
                    answer --;
                }
            }
        }

        return answer;
    }
}