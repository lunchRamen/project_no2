import styled from "styled-components";
import { theme } from "styled-tools";
import { Button, NoticeSection } from "../components";
import { ticket01 } from "../assets/images";
import { useNavigate } from "react-router-dom";

export default function Theater() {
  const navigate = useNavigate();

  const theaterInfo = {
    owner: "하늘",
    linkPath: "https://velog.io/@soryeongk/ReactRouterDomV6",
    intro: {
      title: "마블 덕후들 소개",
      context:
        "마블을 사랑하는 사람들의 모임입니다.\n주 모임 시간은 주말과 평일 20~24시입니다.\n지역은 서울/경기/울산 등 다양합니다.",
    },
    notice: {
      title: "극장 주인 하늘님의 공지사항",
      context:
        "마블 덕후들 환영합니다~\n이번 주 9일 17시~19시 비대면 번개 아이언맨3 정주행 모임 있습니다!자세한 내용은 위의 티켓을 클릭하여 오픈카톡링크로 들어와주세요",
    },
  };

  return (
    <Wrapper>
      <span>
        식스맨 비대면 소극장 <Title>마블 덕후들</Title>입니다.
        <br />
        아래 티켓을 누르면 오픈 카톡 링크로 이동합니다!
      </span>
      <a href={theaterInfo.linkPath}>
        <Image src={ticket01} alt="ticket image" />
      </a>
      <NoticeSection introData={theaterInfo.intro} noticeData={theaterInfo.notice} />
      <Button isMini={true} onClick={() => navigate(-1)}>
        소극장 더 둘러보기
      </Button>
    </Wrapper>
  );
}

const Wrapper = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 12rem;
  padding-bottom: 50rem;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}

  & > span {
    text-align: center;
  }
`;

const Image = styled.img`
  margin: 3rem 0;
  border: 0.1rem solid ${theme("colors.mainBlack")};
  border-radius: 2rem;
  width: 120rem;
  height: 40rem;

  &:hover {
    border-color: ${theme("colors.mainPoint")};
    ${theme("neons.boxNeonGold")}
  }
`;

const Title = styled.span`
  position: relative;
  color: ${theme("colors.mainPoint")};
  margin: 0 0.8em;

  &::before {
    position: absolute;
    content: '"';
    left: -0.5em;
  }

  &::after {
    position: absolute;
    content: '"';
    right: -0.5em;
  }
`;
