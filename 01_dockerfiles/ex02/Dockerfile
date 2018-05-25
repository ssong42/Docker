FROM ruby

RUN apt-get update
RUN apt-get install -y sqlite3 
RUN apt-get install -y nodejs
RUN gem install rails
# copy the app into the directory
COPY app /opt/app
WORKDIR /opt/app 
#the gemfile in this app is outdated so I am using bundle update to get the latest version of the gems and it works
ONBUILD RUN bundle update
ONBUILD EXPOSE 3000

#rake the migrations
ONBUILD RUN rake db:migrate
#loads the data from db/seeds.rb
ONBUILD RUN rake db:seed

#docker build -t ft_rails .
#docker build -f Dockerfile_app -t ex02 .
#docker run -p 3000:3000 ex02
