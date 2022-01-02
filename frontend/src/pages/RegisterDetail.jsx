import { Button, PosterList, SelectList } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { useNavigate } from "react-router-dom";
import Fade from "react-reveal/Fade";
const TEMP_SELECTION_DATA = [
  {
    id: "job",
    label: "님이 어떤 일을 하시는 분인지 궁금해요!",
    option_list: [
      { id: 0, value: "직업 1" },
      { id: 1, value: "직업 2" },
      { id: 2, value: "직업 3" },
      { id: 3, value: "직업 3" },
      { id: 4, value: "직업 4" },
    ],
  },
  {
    id: "location",
    label: "어디에 거주하시나요?",
    option_list: [
      { id: 0, value: "주거 1" },
      { id: 1, value: "주거 2" },
      { id: 2, value: "주거 3" },
      { id: 3, value: "주거 3" },
      { id: 4, value: "주거 4" },
    ],
  },
  {
    id: "time",
    label: "주로 어떤 시간대에 영상을 시청하시나요??",
    option_list: [
      { id: 0, value: "시간대 1" },
      { id: 1, value: "시간대 2" },
      { id: 2, value: "시간대 3" },
      { id: 3, value: "시간대 3" },
      { id: 4, value: "시간대 4" },
    ],
  },
];

export default function RegisterDetail() {
  const navigate = useNavigate();

  return (
    <StWrapper>
      <Fade>
        <StIntro>
          님에게 꼭 맞는 비대면 극장을 추천해드릴게요!
          <br />
          기본적인 정보만을 수집하고, 분석 이외의 목적으로는 절대 사용되지 않습니다.
        </StIntro>

        <SelectList data={TEMP_SELECTION_DATA} />
        <StIntro>다음 중 가장 좋아하는 또는 재밌을 것 같은 영화 6가지를 선택해주세요!</StIntro>
        <PosterList />
        <Button isMini={false} onClick={() => navigate("/register/done")}>
          식스맨 입장을 위한 준비가 완료되었어요!
        </Button>
      </Fade>
    </StWrapper>
  );
}

const StWrapper = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10rem;
  padding-top: 12rem;
  padding-bottom: 50rem;
`;

const StIntro = styled.span`
  text-align: center;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}
`;

export const Select = styled.select`
  border: 0.1rem solid ${theme("colors.mainWhite")};
  background-color: black;
  width: ${({ selectWidth }) => selectWidth};
  height: 4rem;
  color: white;
  font-family: NotoSerif;
  ${theme("fonts.textP")}
  ${theme("neons.boxNeonGold")}
`;
