<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/krislette/square">
    <img src="https://github.com/user-attachments/assets/e885d78f-f24f-4cef-8a4a-6a9276890a42" alt="Logo" width="140" height="140">
  </a>

  <h1 align="center">Square</h1>
  <p align="center">
    A mini-programming language
    <br />
    <a href="https://drive.google.com/file/d/1oMDo13Kc-LLzYHqOMS0kJsGHQaHVEd6C/view?usp=sharing"><strong>Explore the paper »</strong></a>
    <br />
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/krislette/square/issues">Report Bug</a>
    ·
    <a href="https://github.com/krislette/square/issues">Request Feature</a>
  </p>
</div>

<!-- PROJECT DEMO -->
## Demo
<div align="center">
  <img src="" alt="Demo" width="20%">
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Square is a programming language designed with beginners in mind. Its syntax is built around square brackets where its name is derived from, to maintain simplicity and clarity. 
This general programming language emphasizes ease of learning and readability, to make it an ideal starting point for those who are just beginning their programming journey. 
The programming language draws inspiration from C for its robust static typing and fast compile time, to make sure efficient performance and reduced runtime errors. 

<!-- TABLE OF CONTENTS -->
## Table Of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
    <ul>
      <li><a href="#table-of-contents">Table Of Contents</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#technologies">Technologies Used</a></li>
    </ul>
  </li>
  <li>
    <a href="#application-snapshots">Application Snapshots</a>
  </li>
  <li>
    <a href="#installation">Installation</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
    </ul>
  </li>
  <li>
    <a href="#run">Run</a>
  </li>
  <li>
    <a href="#contributors">Contributors</a>
  </li>
  <li>
    <a href="#license">License</a>
  </li>
</ol> 

<!-- FEATURES -->
## Features
### Application
- **Landing Page**: An introduction to the Square language, providing a clean and user-friendly interface.
- **Interactive Terminal**: A terminal where users can test Square language commands and see outputs in real-time.
- **Lexeme Table**: A search feature for exploring the language's syntax and definitions.
- **Theme Switching**: Users can toggle between light and dark themes for a customizable experience.
### Language

#### 1. Square Bracket-Based Syntax
- Core syntax built around `[]` brackets for code blocks
- Clean, visually distinct structure
- Consistent block delimiters across all constructs
```square
fun example() -> void [
    # Code block here
]
```

#### 2. Junction
- Innovative "junction" operator for cleaner OR conditions
- Reduces code redundancy
- More readable conditional logic
```square
# Traditional way in other languages:
if x == 12 or x == 13 or x == 0:
    print("Valid value")

# Square's way:
when [
    x == 12 | 13 | 0 :: print("Valid value")
]
```

#### 3. Batch Field Access
- Access multiple struct/model fields simultaneously
- Reduces boilerplate code
- More efficient field updates
```square
# Traditional way:
user.name = "John"
user.age = 25

# Square's way:
user.[name, age] = ["John", 25]
```

#### 4. Strong Type System
- Explicit type annotations using colon syntax
- Compile-time error catching
- Clear variable declarations
```square
username: str = "john_doe"
age: int = 25
temperature: float = 98.6
```

#### 5. Model System
- Modern take on structured data types
- Type-safe field declarations
- Default value support
```square
mod user [
    name: str = "Guest"
    age: int = 0
    active: bool = true
]
```

<!-- TECHNOLOGIES USED -->
## Technologies

- **[React + Vite](https://reactjs.org/)**: Main framework for building the user interface, utilizing Vite for faster development and building with modern tooling and hot module replacement.  
- **[Python](https://www.python.org/)**: A versatile and powerful programming language used for backend development, known for its simplicity and extensive libraries.  
- **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints.  

### Deployment and Hosting
- **[Netlify](https://www.netlify.com/)**: A powerful platform for deploying and hosting modern web applications, offering continuous deployment, serverless functions, and global CDN for fast performance.
- **[Vercel](https://vercel.com/)**: A cutting-edge platform for deploying and hosting modern web applications, providing seamless continuous deployment, serverless functions, and a global edge network for blazing-fast performance and scalability.

### Development Tools  
- **[Git](https://git-scm.com/)**: Distributed version control system for tracking code changes and collaboration.  
- **[GitHub](https://github.com/)**: Platform for hosting Git repositories, enabling collaborative development and version control.  
- **[Node.js](https://nodejs.org/)**: JavaScript runtime environment for executing server-side code and building scalable applications.  
- **[npm](https://www.npmjs.com/)**: Package manager for JavaScript, used to install and manage dependencies.  
- **[VS Code](https://code.visualstudio.com/)**: Recommended code editor with powerful features like IntelliSense, debugging, and extensions for efficient development.
   
<!-- APPLICATION SNAPSHOTS -->
## Application Snapshots
### Landing Page
![image](https://github.com/user-attachments/assets/4cc6fe7f-43a4-4ac5-a530-7e8f5639b949)

### Terminal
![image](https://github.com/user-attachments/assets/767f0c46-5ed8-4c86-b2d4-925cde5895bd)
![image](https://github.com/user-attachments/assets/c014e4df-ec4b-4593-a09a-bb3a5a7480d7)

### Terminal Themes
#### Dark Mode
<div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
  <img src="https://github.com/user-attachments/assets/c014e4df-ec4b-4593-a09a-bb3a5a7480d7" style="width: 32%; height: auto;"/>
  <img src="https://github.com/user-attachments/assets/217a0d7a-dda3-4a3d-b809-1b8058ee4654" style="width: 32%; height: auto;"/>
  <img src="https://github.com/user-attachments/assets/b31a1d47-7140-4296-a94c-21b1dea977f0" style="width: 32%; height: auto;"/>
</div>

#### Light Mode
<div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
  <img src="https://github.com/user-attachments/assets/54374756-e652-42fe-94e1-b84f1ccedfc3" style="width: 32%; height: auto;"/>
  <img src="https://github.com/user-attachments/assets/7f7f07a7-e571-4965-ac35-3515b09d83cf" style="width: 32%; height: auto;"/>
  <img src="https://github.com/user-attachments/assets/0de188fe-f9eb-41ba-8c4f-022b079fc747" style="width: 32%; height: auto;"/>
</div>

<!-- INSTALLATION -->
## Installation
### Prerequisites

<!-- HOW TO RUN THE PROGRAM -->
##  Run

<!-- Contributor's Table -->
## Contributors
<table style="width: 100%; text-align: center;">
    <thead>
      <tr>
        <th>Name</th>
        <th>Avatar</th>
        <th>GitHub</th>
        <th>Contributions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Acelle Krislette Rosales</td>
        <td><img src="https://avatars.githubusercontent.com/u/143507354?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/krislette">krislette</a></td>
        <td>
          <b>Lead Developer:</b> Acelle oversaw the entire development process, created the lexer, and managed the tokenization process, converting features into tokens. 
          Acelle built the backbone of the backend, set up the server, and deployed both the frontend and backend. 
        </td>
      </tr>
      <tr>
        <td>Regina Bonifacio</td>
        <td><img src="https://avatars.githubusercontent.com/u/116869096?s=400&u=43146b191775802d9ab2f0f721b452ffc52c9efa&v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/feiryrej">feiryrej</a></td>
        <td>
          <b>Frontend Developer:</b> Regina is responsible for making the landing page and overall UI refinement across all pages including the terminal and lexeme table. She also name the language. 
        </td>
      </tr>
      <tr>
        <td>Henry James Carlos</td>
        <td><img src="https://avatars.githubusercontent.com/u/71052354?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/hjcarlos">hjcarlos</a></td>
        <td>
          <b>Frontend Developer:</b> Henry is responsible for the interface displaying generated lexemes in the terminal page  and worked on the syntax for operation symbols and 
          for-loop statements in the Square programming language.
        </td>
      </tr>
      <tr>
        <td>Syruz Ken Domingo</td>
        <td><img src="https://avatars.githubusercontent.com/u/141235021?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/sykeruzn">sykeruzn</a></td>
        <td>
          <b>Technical Writer:</b> Syke is assigned to modify the changes in the programming language documentation, proofread, and finalize the content in all sections.
        </td>
      </tr>
      <tr>
        <td>Fervicmar Lagman</td>
        <td><img src="https://avatars.githubusercontent.com/u/116869089?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/perbik">perbik</a></td>
        <td>
          <b>Backend Developer:</b> Fervicmar contributes in the development, particularly in defining and implementing the tokenization process by identifying and 
          categorizing tokens, ensuring accurate lexical analysis.
        </td>
      </tr>
      <tr>
        <td>Duane Kyros Marzan</td>
        <td><img src="https://avatars.githubusercontent.com/u/148748082?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/kyrariii">kyrariii</a></td>
        <td>
          <b>Technical Writer:</b> Kyros is also assigned to modify the changes in the programming language documentation, proofread, and finalize the content in all sections.
        </td>
      </tr>
      <tr>
        <td>Hans Christian Queja</td>
        <td><img src="https://avatars.githubusercontent.com/u/65350664?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/HansQueja">HansQueja</a></td>
        <td>
          <b>Backend Developer:</b> Hans is one of the developers responsible in defining and implementing the tokenization process. He also contributes in identifying and 
          categorizing tokens, standard processes in lexical analysis. He is also responsible for tweaking additional tokens.
        </td>
      </tr>
      <tr>
        <td>Ylana Ong</td>
        <td><img src="https://avatars.githubusercontent.com/u/108628237?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/jellym0on">jellym0on</a></td>
        <td>
          <b>Frontend Developer:</b> Ylana implemented the frontend editor component for code input and the file upload functionality. 
        </td>
      </tr>
    </tbody>
  </table>
</section>

## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See [LICENSE](LICENSE) for more information.

<p align="right">[<a href="#readme-top">Back to top</a>]</p>



