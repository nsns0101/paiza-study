// 전체 예산이 정해져 있다. 
// 최대한 많은 부서의 물품을 구매해 줄 수 있도록 한다.
// 각 부서가 신청한 금액만큼을 모두 지원해 줘야 한다.
// 예를들어, 1000원을 신청한 부서에는 정확히 1000원을 지원 (1000원 보다 적은 금액 지원 불가)
// 부서별로 신청한 금액이 들어 있는 배열 d와 예산 budget이 매개변수로 주어진다.
// 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 
import java.util.Arrays;

class Solution{
	public int solution(int[] d, int budget) {
		int num = 0;
		int sum = 0;

		Arrays.sort(d);	//값을 오름차순 정렬하여 적은 예산부터 지원하기(최대한 많은 곳 지원하기 위해)
		
		for (int i = 0; i < d.length; i++) {
			if(sum + d[i] <= budget){
				sum += d[i];
				num++;
			}
			else
				break;
		}

		return num;
	}
}