//문제 설명
    // 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
    // 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
    // nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
    // 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

// 제한사항
    // nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
    // nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
class Solution {
    public int solution(int[] nums) {
        int answer = 0;             //소수가 되는 경우의 개수
        int n = nums.length;        //주어진 숫자 배열의 길이

        for(int i = 0; i<n-2; i++) {
            for(int j = i+1; j<n-1; j++) {
                for(int k = j+1; k<n; k++) {
                    int sum = nums[i]+nums[j]+nums[k];  // 서로 다른 숫자 3개를 골라 더하기
                    int l =  (int)Math.sqrt(sum);   //Math.sqrt => 제곱근 구하기
                    
                    for(; l>1; l-- ) {
                        if(sum % l==0) break;
                    }
                    if(l==1)answer++;
                }
            }
        }
        return answer;
    }
}