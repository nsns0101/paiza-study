let max = new Map();

// set으로 맵 객체에 삽입
max.set("id", 0);
max.set("이름", "마이클");
max.set("전공", "영문학");
max.set("나이", 25);

// 이차원 배열로 넘겨주는 것도 가능합니다
let michael = new Map([
    ["id", 0],
    ["이름", "마이클"],
    ["전공", "영문학"],
    ["나이", 29]
])

// get으로 맵 객체 조회
console.log(max.get("이름"));       // "마이클"
console.log(michael.get("이름"));   // "마이클"
// delete로 삭제
console.log(max.delete("나이"));    // 삭제가 성공하면 true를 반환

// clear로 맵 안의 프로퍼티 전부삭제
max.clear();