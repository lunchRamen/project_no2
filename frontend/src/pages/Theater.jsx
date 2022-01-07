import styled from "styled-components";
import { theme } from "styled-tools";
import { Button, Notice } from "../components";
import { useLocation, useNavigate } from "react-router-dom";
import { ticket01, ticket02, ticket03, ticket04, ticket05, ticket06, ticket07 } from "../assets/images";

export default function Theater() {
  const TICKET_LIST = [
    { id: 1, ticket: ticket01 },
    { id: 2, ticket: ticket02 },
    { id: 3, ticket: ticket03 },
    { id: 4, ticket: ticket04 },
    { id: 5, ticket: ticket05 },
    { id: 6, ticket: ticket06 },
    { id: 7, ticket: ticket07 },
  ];

  const navigate = useNavigate();
  const { state } = useLocation();
  const theaterInfo = state.theaterInfo;
  const theaterId = theaterInfo.id;
  const ticket = TICKET_LIST[theaterId - 1].ticket;
  const LINK_PATH = "https://kdt-gitlab.elice.io/003-part3-ottservice/team6/project-template";

  const { title, notice } = theaterInfo;

  return (
    <Wrapper>
      <span>
        식스맨 비대면 소극장 <Title>{title}</Title>입니다.
        <br />
        아래 티켓을 누르면 오픈 카톡 링크로 이동합니다!
      </span>
      <a href={LINK_PATH}>
        <Image src={ticket} alt="ticket image" />
      </a>
      {/* <NoticeSection introData={theaterInfo.intro} noticeData={theaterInfo.notice} /> */}
      <Notice title={title}>
        <StNotice>{notice}</StNotice>
      </Notice>
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

export const Title = styled.span`
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

const StNotice = styled.div`
  margin: 1.5rem 0 5rem 0;
  border: 0.1rem solid ${theme("colors.mainPoint")};
  padding: 4rem;
  width: 120rem;
  height: 35.4rem;
  color: ${theme("colors.mainWhite")};
  white-space: pre-wrap;
  ${theme("neons.boxNeonGold")}
  ${theme("fonts.textP")}
`;
