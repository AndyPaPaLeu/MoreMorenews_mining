install.packages("rvest")
library(rvest)
install.package("httr")
library(httr)
install.packages("stringr")
library(stringr)
install.packages("jsonlite")
library(jsonlite)
install.packages("readr")
library(readr)
install.packages("curl")
library(curl)

Title <- c()
Time <- c()
URL <- c()
Author <- c()
IP <- c()
Source <- c()
Text <- c()
Push_num <- c()
Boo_num <- c()
Arrow_num <- c()
Content <- c()
Article_URL <- c()
ptt_url <- c()

ptt_all <- data.frame(Title, Time, URL, Author, IP, Source, Text, Push_num, Boo_num, Arrow_num) 
push_all <- data.frame(Article_URL ,Content)

startPage <- 2001
stopPage <- 3000
for(i in startPage:stopPage) {
  print(i)
  url <- str_c("https://www.ptt.cc/bbs/Gossiping/index", i, ".html")
  ptt_get = read_html(GET(url, set_cookies(over18 = 1)))
  ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='title']/a")
  
  library(stringr)
  current_addr <- str_c("http://www.ptt.cc", html_attr(ptt_nodes,'href'))
  # 網址
  ptt_url <- c(ptt_url, current_addr)
}
  
  for(j in 1:length(ptt_url)){
    ptt_get <- read_html(GET(ptt_url[j], set_cookies(over18 = 1)))
    ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='article-meta-value']")
    post_4items <- html_text(ptt_nodes, trim = T)
    #若非文章類型 (ex:投票) 即直接下一篇
    if(length(post_4items)!=0){
      if(!grepl("[公告]",post_4items[3])){
      # 標題
      ptt_title <- post_4items[3]
      # 作者
      ptt_author <- strsplit(post_4items[1], " ")[[1]][1]
      # 來源
      source <- post_4items[2]
      # 時間
      ptt_time <- post_4items[4]
      
      #內文
      ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='bbs-screen bbs-content']")
      target <- html_text(ptt_nodes)
      target2 <- strsplit(target, split=post_4items[4],fixed=T)[[1]][2]
      target3 <- strsplit(target2,split="\n--\n",fixed=T)[[1]][1]
      target_sep <- strsplit(target3,split="\n-----\n",fixed=T)[[1]][1]
      ## 內文 - first (text) 
      target_context <- strsplit(target_sep,split="\n\n",fixed=T)
      ## 內文 - findout the first line
      target_context2 <- strsplit(target_context[[1]],split='\n',fixed=T)
     # if (grepl(": ",target_context2[[1]][[length(target_context2[[1]])]])){
     #    r_first_line <- "" 
     #  } else {
     #    r_first_line <- target_context2[[1]][[length(target_context2[[1]])]]
     #  }
      
      ## 內文 - text vector cleaning and conbining
      clean <-function(x) {
        x <- x[!grepl(": ",x)]
        x <- x[!grepl("※ 引述《",x)]
        x <-x[nchar(x)>0]
      }
      cleaned_list <- lapply(target_context2,clean)
      conbined_list <- lapply(cleaned_list,paste)
      conbined_vector <- paste(cleaned_list)
      conbined_text <-paste(conbined_vector[1:length(conbined_vector)],collapse ="")
      ## 內文 - text cleaning
      x <- conbined_text 
      x <- gsub("(character)\\(0)",replacement="",x)
      x <- gsub('c\\(\\\"',replacement="",x) 
      x <- gsub('\", \"',replacement="，",x)  # \", \"
      x <- gsub('\")',replacement="",x)       # \")
      x <- gsub('http([0-9a-zA-Z]|[[:punct:]])+',replacement="",x) 
      x <- gsub('XD+',replacement="XD",x) 
      x <- gsub('[[:punct:]]{2,}',replacement=" ",x) 
      x <- gsub('[[:space:]]+',replacement="，",x) 
      ptt_text <- gsub(', ',replacement="，",x)
      
      
      
      # IP
      ptt_nodes2 <- html_nodes(ptt_get,xpath = "//*[@class='f2']")
      ip <- paste((html_text(ptt_nodes2, trim = T)), collapse = "")
      ptt_ip <- strsplit(strsplit(ip, "來自: ")[[1]][2], "※ 文")[[1]][1]
      # 推文數
      ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='hl push-tag']")
      push_num <- length(ptt_nodes)
      # 噓數及→數
      ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='f1 hl push-tag']")
      boo_num <- str_count(paste(html_text(ptt_nodes, trim = T), collapse = ""), "噓")
      arrow_num <- str_count(paste(html_text(ptt_nodes, trim = T), collapse = ""), "→")
      
      # 存入ptt_all data.frame
      y <- data.frame (Title=ptt_title, Time=ptt_time, URL=ptt_url[j], Author=ptt_author, IP=ptt_ip, Source=source, Text=ptt_text, Push_num=push_num, Boo_num=boo_num, Arrow_num=arrow_num)
      ptt_all <- rbind(ptt_all, y)
     
      # 推文內容
      ptt_nodes <- html_nodes(ptt_get,xpath = "//*[@class='push']")
      nodes_trim <- html_text(ptt_nodes, trim = T)
      push_text <- substring(nodes_trim, 1, nchar(nodes_trim)-11)
      if (length(push_text)!=0){
        push_detail <- data.frame (Ariticle_URL=ptt_url[j], Contect=push_text)
        push_all <- rbind(push_all, push_detail)
      }
      }
    }
    # 確認目前進度
    print(length(ptt_url)-j)
    
  }
ptt_all %>% toJSON() %>% write_lines(str_c("PTT_",startPage,"_",stopPage,".json"))
push_all %>% toJSON() %>% write_lines(str_c("Push_",startPage,"_",stopPage,".json"))


# 讀入上面存好的json
# PTT_fromJSON <- fromJSON(str_c("PTT_",startPage,"_",stopPage,".json"))
# PTT_Push_fromJSON <- fromJSON(str_c("Push_",startPage,"_",stopPage,".json"))


