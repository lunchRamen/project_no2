import { useLocation } from "react-router-dom";
import styled, { css } from "styled-components";
import { ifProp, theme } from "styled-tools";
import { CommonNav } from "..";
import { LogoMini } from "../../assets/icons";
import { Link } from "react-router-dom";
const NAVS = {
  register: "회원가입",
  login: "로그인",
};

const Header = () => {
  const location = useLocation();
  const pathname = location.pathname.split("/")[1];

  const isCommon = pathname === "register" ? false : pathname === "login" ? false : true;

  return (
    <StWrapper isLanding={!pathname} isCommon={isCommon}>
      <Link to={"/main"}>
        <LogoMini />
      </Link>
      {isCommon ? <CommonNav /> : <StListWrapper>{NAVS[pathname]}</StListWrapper>}
      <span id="logout">로그아웃</span>
    </StWrapper>
  );
};

export default Header;

const StWrapper = styled.header`
  ${ifProp(
    { isLanding: true },
    css`
      display: none;
    `,
    css`
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-right: 10rem;
      width: 100%;
      height: 8rem;
      ${theme("fonts.textH2")}
      ${theme("neons.textNeonGold")};

      & > span#logout {
        visibility: ${ifProp({ isCommon: true }, "visible", "hidden")};
      }
    `,
  )};
`;

export const StListWrapper = styled.nav`
  display: flex;
  justify-content: center;
`;
