import styled from "styled-components";
import { theme } from "styled-tools";

const Header = () => {
  return <StWrapper>헤더</StWrapper>;
};

export default Header;

const StWrapper = styled.p`
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}
`;
