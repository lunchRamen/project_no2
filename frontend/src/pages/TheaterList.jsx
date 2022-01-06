import axios from "axios";
import styled from "styled-components";
import { theme } from "styled-tools";
import { Table } from "../components";
import { Input } from "../components/registerDetail/BasicSelect";

const tHeadList = ["극장 개관일", "극장이름", "극장주인", "관객 수", "주요 관심 장르"];
// const tBodyList = [
//   { id: 0, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
//   { id: 1, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
//   { id: 2, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
//   { id: 3, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
//   { id: 4, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
//   { id: 5, contents: ["21.12.24", "마블덕후들", "하늘", "12/30", "액션/SF"] },
// ];
const tBodyList = await axios
  .get("http://127.0.0.1:8000/small-theater")
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });

export function getData() {
  return tBodyList;
}

export default function TheaterList() {
  return (
    <Wrapper>
      <InputWrapper>
        <label>님과 비슷한 취향을 가진 사람들을 찾아볼까요?</label>
        <SearchInput type="text" placeholder="영화 제목 또는 장르를 입력해보세요!" />
      </InputWrapper>
      <TableWrapper>
        <span>전체 소극장 목록</span>
        <Table tHeadList={tHeadList} tBodyList={tBodyList} />
      </TableWrapper>
    </Wrapper>
  );
}

const Wrapper = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 10rem;
`;

const InputWrapper = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 5rem;
  width: 144rem;
  color: ${theme("colors.mainPoint")};
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH2")}
`;

const SearchInput = styled(Input)`
  padding: 1.5rem 2rem;
  width: 69.5rem;
  height: 6rem;
`;

const TableWrapper = styled.section`
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH2")}
`;
