import { Link } from "react-router-dom";

function LandingPage() {
  return (
    <div className="about-page">
      <div className="square__header section__padding" id="about">
        <div className="square__header-content">
          <h1 className="gradient__text">
            Revolutionize Your Development Process with Square
          </h1>
          <p>
            Square is a programming language designed with beginners in mind, particularly targeting
            high school students, computer science and IT students especially freshmen, and career shifters
            who are new to coding.
          </p>
          
          <div className="button-container">
            <Link 
              to="/home" 
              style={{ textDecoration: "none", color: "inherit" }} 
              className="custom__button"
            >
              <span className="button__background"></span>
              <div className="button__content">
                <span>Go to Terminal</span>
                <svg
                  fill="none"
                  height="16"
                  viewBox="0 0 24 24"
                  width="16"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M10.75 8.75L14.25 12L10.75 15.25"
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="1.5"
                  />
                </svg>
              </div>
            </Link>

            <a 
                href="https://drive.google.com/paper-link" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="custom__button">
                <span className="button__background"></span>
                    <div className="button__content">
                        <span>View Our Paper</span>
                            <svg
                                fill="none"
                                height="16"
                                 viewBox="0 0 24 24"
                                width="16"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                   d="M10.75 8.75L14.25 12L10.75 15.25"
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="1.5"
                                />
                            </svg>
                        </div>
               </a>
          </div>
        </div>

        <div className="square__header-image">
          {/* ! Put image here */}
          <img src="sqr-logo.png" alt="Square Programming" />
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
