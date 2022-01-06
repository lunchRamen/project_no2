import React, { useState } from "react";
import axios from "axios";
import styled from "styled-components";
import { theme } from "styled-tools";
import { Table } from "../components";
import { Input } from "../components/registerDetail/BasicSelect";

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
  const [inputValue, setInputValue] = useState("");
  const [result, setResult] = useState([]);
  const [genre, setGenre] = useState("");

  const handleClick = (e) => {
    setGenre(e.target.value);
    const response = async () => await axios.get("api/small-theater/");
    const data = response.data;
    setResult(data);
    console.log(genre);
  };

  const handleSubmit = (e) => {
    if (e.key === "Enter") {
      const response = async () => await axios.post("api/small-theater", { inputValue });
      const data = response.data;
      console.log(result);
      setResult(data);
    }
  };

  return (
    <Wrapper>
      <InputWrapper>
        <label>님과 비슷한 취향을 가진 사람들을 찾아볼까요?</label>
        <form>
          <SearchInput
            type="text"
            placeholder="영화 제목 또는 장르를 입력해보세요!"
            name="title"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleSubmit}
          />
          <Searchbutton type="submit" value="검색" />
        </form>
      </InputWrapper>
      <InputWrapper>
        <Searchbutton type="button" value="로맨스" onClick={handleClick} />
        <Searchbutton type="button" value="액션" onClick={handleClick} />
        <Searchbutton type="button" value="공포" onClick={handleClick} />
        <Searchbutton type="button" value="스릴러" onClick={handleClick} />
        <Searchbutton type="button" value="SF" onClick={handleClick} />
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
  width: 45rem;
  height: 6rem;
`;
const Searchbutton = styled.input`
  padding: 1.5rem 2rem;
  width: 15rem;
  height: 6rem;
  cursor: pointer;
  border: 0.1rem solid ${theme("colors.mainWhite")};
  color: white;
  font-family: NotoSerif;
  ${theme("fonts.textP")}
  ${theme("neons.boxNeonGold")}
`;

const TableWrapper = styled.section`
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH2")}
`;
