import { Table } from "../components";

const tHeadList = ["극장 개관일", "극장이름", "극장주인", "관객 수", "주요 관심 장르"];
const tBodyList = [
  { id: 0, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  { id: 1, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  { id: 2, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  { id: 3, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  { id: 4, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
  { id: 5, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
];

export default function TheaterList() {
  return <Table tHeadList={tHeadList} tBodyList={tBodyList} />;
}
