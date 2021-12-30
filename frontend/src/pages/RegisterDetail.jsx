import { PosterList } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { Link } from "react-router-dom";
export default function RegisterDetail() {
  return (
    <>
      <Intro>
        <p>님에게 꼭 맞는 비대면 극장을 추천해드릴게요!</p>
        <p>기본적인 정보만을 수집하고, 분석 이외의 목적으로는 절대 사용되지 않습니다.</p>
      </Intro>
      <Wrap>
        <Age>
          나이&nbsp;&nbsp;<Input type="text"></Input>&nbsp;&nbsp;&nbsp;&nbsp; 성별&nbsp;&nbsp;
          <SelectG name="gender" form="Gender" placeholder="성별">
            <option value="1">남자</option>
            <option value="0">여자</option>
          </SelectG>
        </Age>
        <IdWrap>
          님이 어떤 일을 하시는 분인지 궁금해요!
          <Select name="job" form="Job" style={{ width: "50rem" }}>
            <option value="0">1</option>
            <option value="1">2</option>
            <option value="2">3</option>
            <option value="3">4</option>
            <option value="4">5</option>
            <option value="5">6</option>
          </Select>
          어디에 거주하시나요?
          <Select name="living" form="Living" style={{ width: "50rem" }}>
            <option value="0">1</option>
            <option value="1">2</option>
            <option value="2">3</option>
            <option value="3">4</option>
            <option value="4">5</option>
            <option value="5">6</option>
          </Select>
          주로 어떤 시간대에 영상을 시청하시나요?
          <Select name="time" form="Time" style={{ width: "50rem" }}>
            <option value="0">1</option>
            <option value="1">2</option>
            <option value="2">3</option>
            <option value="3">4</option>
            <option value="4">5</option>
            <option value="5">6</option>
          </Select>
        </IdWrap>
        <p>다음 중 가장 좋아하는 또는 재밌을 것 같은 영화 6가지를 선택해주세요!</p>

        <Link to="/register/done">
          <LandingButton isMini={true}>로그인</LandingButton>
        </Link>
      </Wrap>
      <footer>
        <PosterList />
      </footer>
    </>
  );
}
const Intro = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 40vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};
`;

const Wrap = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 30vh;
  ${theme("fonts.textH2")} ${theme("neons.textNeonGold")};
`;
const IdWrap = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 5rem;
  ${theme("fonts.textH3")}
  ${theme("neons.textNeonGold")};
`;

// const PassWrap = styled.div`
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
//   margin-bottom: 5rem;
//   ${theme("fonts.textH3")}
//   ${theme("neons.textNeonGold")};
// `;

// const PassconWrap = styled.div`
//   display: flex;
//   flex-direction: column;
//   justify-content: center;
//   margin-bottom: 3rem;
//   ${theme("fonts.textH3")}
//   ${theme("neons.textNeonGold")};
// `;

const Input = styled.input`
  width: 20rem;
  border-radius: 2rem;
  color: white;
  ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
`;

const SelectG = styled.select`
  width: 10rem;
  height: 4rem;
  background-color: black;
  color: white;
  font-size: 2rem;
  text-align: center;
  border-radius: 2rem;

  ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
`;
const Select = styled.select`
  width: 10rem;
  height: 4rem;
  background-color: black;
  color: white;
  font-size: 2rem;
  text-align: center;
  border-radius: 2rem;
  margin-bottom: 5rem;
  ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
`;
const Age = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 30vh;
  margin-bottom: 5rem;
  ${theme("fonts.textH2")} ${theme("neons.textNeonGold")};
`;

const LandingButton = styled.span`
  cursor: pointer;
  border-bottom: 0.1rem solid ${theme("colors.mainBlack")};
  padding: 2rem 3.5rem;
  color: ${theme("colors.mainWhite")};
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH3")}

  &:hover {
    color: ${theme("colors.mainPoint")};
    border-color: ${theme("colors.mainPoint")};
  }
`;
