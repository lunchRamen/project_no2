import styled from "styled-components";
import { theme } from "styled-tools";
import { Notice } from "..";

export default function NoticeSection({ introData, noticeData }) {
  return (
    <StNoticeWrapper>
      <Notice title={introData.title}>
        <StNotice>{introData.context}</StNotice>
      </Notice>
      <Notice title={noticeData.title}>
        <StNotice>{noticeData.context}</StNotice>
      </Notice>
    </StNoticeWrapper>
  );
}

const StNoticeWrapper = styled.section`
  display: flex;
  justify-content: space-between;
  margin-bottom: 9rem;
  width: 144rem;

  & > section {
    color: ${theme("colors.mainPoint")};
  }
`;

const StNotice = styled.div`
  margin-top: 1.5rem;
  border: 0.1rem solid ${theme("colors.mainPoint")};
  padding: 4rem;
  width: 70rem;
  height: 35.4rem;
  color: ${theme("colors.mainWhite")};
  white-space: pre-wrap;
  ${theme("neons.boxNeonGold")}
  ${theme("fonts.textP")}
`;
