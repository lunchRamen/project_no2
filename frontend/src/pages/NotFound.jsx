import { Button, Table } from "../components";

export default function NotFound() {
  const handleClick = () => {
    // 버튼 클릭 시에 하고 싶은 일들을 여기에 정의
    console.log("clicked!");
  };

  const tHeadList = ["극장 개관일", "극장이름", "극장주인", "관객 수", "주요 관심 장르"];
  const tBodyList = [
    { id: 0, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
    { id: 1, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
    { id: 2, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
    { id: 3, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
    { id: 4, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
    { id: 5, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  ];

  return (
    <div>
      {/* 작은 버튼들 */}
      <Button isMini={true} onClick={handleClick}>
        결정
      </Button>
      {/* 크거나 길쭉한 버튼들 */}
      <Button isMini={false} onClick={handleClick}>
        식스맨 입장을 위한 준비가 완료되었어요!
      </Button>
      <Table tHeadList={tHeadList} tBodyList={tBodyList} />
    </div>
  );
}
