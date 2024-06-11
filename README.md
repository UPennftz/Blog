# Blog
Source Code Backup for Master Course Projects in University of Glasgow

## English Version

### Project Information

#### Project Structure
This project consists of two main parts: `blog-backend` and `blog-frontend`.

##### blog-backend
- **Functionality**: Provides backend services for the blog.
- **Tech Stack**: Built with Node.js and Express.
- **Main Files and Directories**:
  - `app.js`: The application entry file that configures and starts the Express server.
  - `routes/`: Defines API routes and handles client requests.
    - `index.js`: Main routing file containing all API endpoints.
  - `models/`: Defines data models, using Mongoose to connect to MongoDB.
    - `User.js`: User data model.
    - `Post.js`: Blog post data model.
  - `controllers/`: Handles business logic.
    - `userController.js`: Business logic related to users.
    - `postController.js`: Business logic related to blog posts.
  - `config/`: Configuration files, including database connection settings.
    - `db.js`: Database connection configuration.
  - `node_modules/`: Project dependencies.

##### blog-frontend
- **Functionality**: Provides the frontend interface for the blog.
- **Tech Stack**: Built with React and Redux.
- **Main Files and Directories**:
  - `src/`: Source code directory.
    - `index.js`: Application entry file, renders the root component.
    - `App.js`: Root application component, defines routes and overall layout.
  - `src/components/`: React components responsible for the UI.
    - `Header.js`: Top navigation bar component.
    - `PostList.js`: Blog post list component.
    - `PostDetail.js`: Blog post detail component.
  - `src/redux/`: Redux state management files.
    - `store.js`: Configures the Redux store.
    - `reducers/`: Redux reducers, handle state changes.
      - `postReducer.js`: Handles blog post-related state.
      - `userReducer.js`: Handles user-related state.
    - `actions/`: Redux actions, define action types and actions.
      - `postActions.js`: Blog post-related actions.
      - `userActions.js`: User-related actions.
  - `public/`: Static resource directory, contains the HTML template and other static files.

#### Project Description

This is a full-stack blog application example. The frontend is built using React for the user interface, and Redux for state management, while the backend is built using Node.js and Express to provide API services. The project demonstrates a decoupled frontend-backend architecture, where the frontend interacts with the backend through API calls.

- **Frontend**: React is used to build the user interface, with Redux managing the state, allowing for convenient state sharing and management across components.
- **Backend**: Node.js and Express handle API requests, using Mongoose to connect to MongoDB for data storage.

The project includes user authentication and CRUD (Create, Read, Update, Delete) operations for blog posts. It serves as a useful reference for learning how to build a full-stack application.

## 中文版说明

### 项目信息

#### 项目结构
这个项目包含两个主要部分：`blog-backend` 和 `blog-frontend`。

##### blog-backend后端部分
- **功能**: 提供博客的后端服务。
- **技术栈**: 使用 Node.js 和 Express 构建。
- **主要文件和目录**:
  - `app.js`: 应用入口文件，配置并启动Express服务器。
  - `routes/`: 定义API路由，处理客户端请求。
    - `index.js`: 主路由文件，包含所有API端点。
  - `models/`: 数据模型定义，使用 Mongoose 连接 MongoDB。
    - `User.js`: 用户数据模型。
    - `Post.js`: 博客文章数据模型。
  - `controllers/`: 处理业务逻辑。
    - `userController.js`: 用户相关的业务逻辑。
    - `postController.js`: 博客文章相关的业务逻辑。
  - `config/`: 配置文件，存放数据库连接等配置信息。
    - `db.js`: 数据库连接配置。
  - `node_modules/`: 项目依赖库。

##### blog-frontend前端部分
- **功能**: 提供博客的前端界面。
- **技术栈**: 使用 React 和 Redux 构建。
- **主要文件和目录**:
  - `src/`: 源代码目录。
    - `index.js`: 应用入口文件，渲染根组件。
    - `App.js`: 应用根组件，定义路由和整体布局。
  - `src/components/`: React组件，负责页面UI。
    - `Header.js`: 顶部导航栏组件。
    - `PostList.js`: 博客文章列表组件。
    - `PostDetail.js`: 博客文章详情组件。
  - `src/redux/`: Redux状态管理相关文件。
    - `store.js`: 配置 Redux store。
    - `reducers/`: Redux reducers，处理状态变化。
      - `postReducer.js`: 处理博客文章相关状态。
      - `userReducer.js`: 处理用户相关状态。
    - `actions/`: Redux actions，定义操作类型和操作。
      - `postActions.js`: 博客文章相关操作。
      - `userActions.js`: 用户相关操作。
  - `public/`: 静态资源目录，包含 HTML 模板和其他静态文件。

#### 项目说明

这是一个全栈博客应用示例，前端使用 React 构建用户界面，后端使用 Node.js 和 Express 提供 API 服务。项目展示了前后端分离的开发模式，前端通过调用后端提供的 API 实现数据交互。

- **前端部分**: React 负责构建用户界面，Redux 用于状态管理，使得组件间状态共享和管理更加便捷。
- **后端部分**: Node.js 和 Express 负责处理 API 请求，使用 Mongoose 连接 MongoDB 进行数据存储。

项目示例包括用户认证、博客文章的创建、读取、更新和删除 (CRUD) 操作，适合用于学习和参考如何构建一个全栈应用。
