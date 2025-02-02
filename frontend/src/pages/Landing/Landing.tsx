import { Link } from "react-router-dom";
import { useEffect } from "react";

function LandingPage() {
  useEffect(() => {
    document.body.classList.add("no-scroll");

    return () => {
      document.body.classList.remove("no-scroll");
    };
  }, []);

  return (
    <div className="about-page">
      <div className="square__header section__padding" id="about">
        <div className="spotlight-shine"></div>

        <div className="square__header-content">
          <h1 className="gradient__text">
            Revolutionize Your Development Process with Square
          </h1>
          <p>
            Square is a programming language designed with beginners in mind, particularly targeting
            high school students, computer science and IT students especially freshmen, and career shifters
            who are new to coding.
          </p>

          <div className="button-group">
            <Link to="/home" className="btn primary">
              Go to Terminal
            </Link>
            <a href="https://drive.google.com/file/d/1oMDo13Kc-LLzYHqOMS0kJsGHQaHVEd6C/view?usp=sharing" target="_blank" rel="noopener noreferrer" className="btn secondary">
              View Our Paper
            </a>
          </div>
        </div>

        <div className="square__header-image">
          <img src="sqr.png" alt="Square Programming" />
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
