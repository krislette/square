import './About.css';

export default function About() {
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
                </div>

                <div className="square__header-image">
                    // ! Put image here 
                    <img src="path_to_your_image.jpg" alt="Square Programming" />
                </div>
            </div>
        </div>
    );
}
